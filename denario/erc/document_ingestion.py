from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence

from cmbagent import preprocess_task

from ..config import (
    INPUT_FILES,
    CALL_DOCS_DIR,
    APPLICANT_DOCS_DIR,
    PRIOR_RESULTS_DOCS_DIR,
)

ALLOWED_DOC_EXTENSIONS = {".md", ".markdown", ".txt", ".tex", ".rst", ".pdf"}

CALL_DOCS_INSTRUCTIONS = """
You are preparing an internal brief of the ERC call documents. Extract only the information that proposal-writing agents
need: identifiers, panel focus, evaluation criteria, eligibility constraints, page limits, deadlines, and any mandatory annexes.
Return markdown with clear subsections for `Call Overview`, `Evaluation Criteria`, `Mandatory Material`, and `Constraints & Deadlines`.
"""

APPLICANT_DOCS_INSTRUCTIONS = """
Summarize the applicant CVs, host letters, and supporting material into a concise team profile for an ERC proposal.
Highlight the PI credentials, key achievements, leadership experience, available infrastructure, collaborators, and mentoring plans.
Return markdown sections titled `Principal Investigator`, `Key Personnel`, `Host Institution Support`, and `Collaboration Network`.
"""

PRIOR_RESULTS_INSTRUCTIONS = """
Capture the prior results or track-record evidence that justifies the ERC project's feasibility.
List landmark publications, datasets, prototypes, or awards and mention how they support the new proposal.
Return markdown sections titled `Breakthrough Results`, `Key Publications & Outputs`, and `Relevance to Proposal`.
"""


def summarize_call_documents(
    project_dir: str,
    document_paths: Sequence[str] | None,
    summarizer_model: str,
    summarizer_response_formatter_model: str,
) -> str:
    """Summarize ERC call documents into a reusable brief."""

    return _summarize_documents(
        project_dir=project_dir,
        document_paths=document_paths,
        default_subdir=CALL_DOCS_DIR,
        summary_instructions=CALL_DOCS_INSTRUCTIONS,
        summarizer_model=summarizer_model,
        summarizer_response_formatter_model=summarizer_response_formatter_model,
    )


def summarize_applicant_documents(
    project_dir: str,
    document_paths: Sequence[str] | None,
    summarizer_model: str,
    summarizer_response_formatter_model: str,
) -> str:
    """Summarize applicant/host documents into a team profile."""

    return _summarize_documents(
        project_dir=project_dir,
        document_paths=document_paths,
        default_subdir=APPLICANT_DOCS_DIR,
        summary_instructions=APPLICANT_DOCS_INSTRUCTIONS,
        summarizer_model=summarizer_model,
        summarizer_response_formatter_model=summarizer_response_formatter_model,
    )


def summarize_prior_results_documents(
    project_dir: str,
    document_paths: Sequence[str] | None,
    summarizer_model: str,
    summarizer_response_formatter_model: str,
) -> str:
    """Summarize prior results or track record material."""

    return _summarize_documents(
        project_dir=project_dir,
        document_paths=document_paths,
        default_subdir=PRIOR_RESULTS_DOCS_DIR,
        summary_instructions=PRIOR_RESULTS_INSTRUCTIONS,
        summarizer_model=summarizer_model,
        summarizer_response_formatter_model=summarizer_response_formatter_model,
    )


def _summarize_documents(
    project_dir: str,
    document_paths: Sequence[str] | None,
    default_subdir: str,
    summary_instructions: str,
    summarizer_model: str,
    summarizer_response_formatter_model: str,
) -> str:
    files = _collect_document_paths(project_dir, document_paths, default_subdir)
    combined_text = _combine_documents(files)
    prompt = f"""{summary_instructions.strip()}

--- SOURCE DOCUMENTS ---
{combined_text}
"""
    return preprocess_task(
        prompt,
        work_dir=project_dir,
        summarizer_model=summarizer_model,
        summarizer_response_formatter_model=summarizer_response_formatter_model,
    )


def _collect_document_paths(
    project_dir: str,
    provided_paths: Sequence[str] | None,
    default_subdir: str,
) -> list[Path]:
    base_input = Path(project_dir) / INPUT_FILES
    base_input.mkdir(parents=True, exist_ok=True)

    resolved_paths: list[Path] = []
    if provided_paths:
        for raw_path in provided_paths:
            candidate = Path(raw_path)
            if not candidate.is_absolute():
                candidate = base_input / candidate
            if not candidate.exists():
                raise FileNotFoundError(f"Document '{candidate}' not found.")
            if candidate.is_dir():
                resolved_paths.extend(_expand_directory(candidate))
            else:
                resolved_paths.append(candidate)
    else:
        folder = base_input / default_subdir
        folder.mkdir(parents=True, exist_ok=True)
        resolved_paths.extend(_expand_directory(folder))

    filtered = [
        path for path in resolved_paths
        if path.is_file() and path.suffix.lower() in ALLOWED_DOC_EXTENSIONS
    ]

    if not filtered:
        default_folder = base_input / default_subdir
        raise FileNotFoundError(
            f"No supported documents found. Provide document_paths explicitly or place files in '{default_folder}'."
        )

    # Ensure deterministic ordering
    filtered.sort()
    return filtered


def _expand_directory(directory: Path) -> list[Path]:
    """Return all files in the directory (non-recursive)."""

    return [child for child in sorted(directory.iterdir()) if child.is_file()]


def _combine_documents(files: Sequence[Path]) -> str:
    blocks: list[str] = []
    for idx, file_path in enumerate(files, start=1):
        content = _read_document(file_path).strip()
        header = f"### Document {idx}: {file_path.name}"
        blocks.append(f"{header}\n\n{content}")
    return "\n\n".join(blocks)


def _read_document(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return _extract_pdf_text(path)
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        return handle.read()


def _extract_pdf_text(path: Path) -> str:
    try:
        import fitz  # type: ignore
    except ImportError as exc:
        raise ImportError(
            "PyMuPDF is required to read PDF documents. Install it via `pip install pymupdf`."
        ) from exc

    text_chunks: list[str] = []
    with fitz.open(path) as doc:
        for page in doc:
            text_chunks.append(page.get_text())
    return "\n".join(text_chunks)
