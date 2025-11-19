from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import cmbagent

from ..key_manager import KeyManager
from ..prompts.erc import ERC_VISION_SYSTEM_PROMPT
from ..utils import create_work_dir, get_task_result


class ERCVisionAgent:
    """Agent that negotiates ERC vision/objectives with maker/critic loop."""

    def __init__(
        self,
        keys: KeyManager,
        work_dir: str | Path,
        idea_maker_model: str = "gpt-4o",
        idea_hater_model: str = "o3-mini",
        planner_model: str = "gpt-4o",
        plan_reviewer_model: str = "o3-mini",
        orchestration_model: str = "gpt-4.1",
        formatter_model: str = "o3-mini",
    ) -> None:
        self.idea_maker_model = idea_maker_model
        self.idea_hater_model = idea_hater_model
        self.planner_model = planner_model
        self.plan_reviewer_model = plan_reviewer_model
        self.orchestration_model = orchestration_model
        self.formatter_model = formatter_model
        self.keys = keys
        self.work_dir = create_work_dir(work_dir, "erc_vision")

    def develop_vision(
        self,
        *,
        call_info: str,
        data_description: str,
        prior_results: str,
        literature_context: str | None = None,
        idea_background: str | None = None,
    ) -> str:
        """Run the maker/critic loop and return markdown with vision + objectives."""

        background_block = ""
        if idea_background:
            background_block = f"\n\n### Idea Background\n{idea_background.strip()}"

        literature_block = ""
        if literature_context:
            literature_block = f"\n\n### Literature Snapshot\n{literature_context.strip()}"

        planning_context = dedent(
            f"""
            ### ERC Call Context
            {call_info.strip()}

            ### Available Data / Resources
            {data_description.strip()}

            ### Prior Results
            {prior_results.strip()}
            {background_block}
            {literature_block}
            """
        )

        results = cmbagent.planning_and_control_context_carryover(
            planning_context,
            n_plan_reviews=1,
            max_plan_steps=6,
            idea_maker_model=self.idea_maker_model,
            idea_hater_model=self.idea_hater_model,
            plan_instructions=ERC_VISION_SYSTEM_PROMPT,
            planner_model=self.planner_model,
            plan_reviewer_model=self.plan_reviewer_model,
            work_dir=self.work_dir,
            api_keys=self.keys,
            default_llm_model=self.orchestration_model,
            default_formatter_model=self.formatter_model,
        )

        chat_history = results["chat_history"]
        task_result = get_task_result(chat_history, "idea_maker_nest")
        return task_result
