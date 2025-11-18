from typing import List, Dict
from pydantic import BaseModel, Field

class Research(BaseModel):
    """Research class."""
    data_description: str = Field(default="", description="The data description of the project")
    """The data description of the project."""
    idea: str = Field(default="", description="The idea of the project")
    """The idea of the project."""
    methodology: str = Field(default="", description="The methodology of the project")
    """The methodology of the project."""
    results: str = Field(default="", description="The results of the project")
    """The results of the project."""
    plot_paths: List[str] = Field(default_factory=list, description="The plot paths of the project")
    """The plot paths of the project."""
    keywords: Dict[str, str] | list = Field(default_factory=dict, description="The keywords describing the project")
    """The keywords describing the project."""


class ERCProposal(Research):
    """ERC proposal-specific data container."""
    call_info: str = Field(default="", description="ERC call details, panel information, and constraints.")
    """ERC call details, panel information, and constraints."""
    vision: str = Field(default="", description="High-level vision or extended synopsis narrative.")
    """High-level vision or extended synopsis narrative."""
    objectives: str = Field(default="", description="List of scientific objectives and ambition statements.")
    """List of scientific objectives and ambition statements."""
    work_packages: str = Field(default="", description="Structured work-package definitions in markdown or JSON.")
    """Structured work-package definitions in markdown or JSON."""
    implementation_plan: str = Field(default="", description="Overall implementation, management, and schedule plan.")
    """Overall implementation, management, and schedule plan."""
    impact_plan: str = Field(default="", description="Impact, communication, and exploitation plan.")
    """Impact, communication, and exploitation plan."""
    team_profile: str = Field(default="", description="PI track record, team composition, and institutional support.")
    """PI track record, team composition, and institutional support."""
    ethics_strategy: str = Field(default="", description="Ethics, risk, and regulatory considerations.")
    """Ethics, risk, and regulatory considerations."""
    budget_overview: str = Field(default="", description="Budget summary narrative or tables.")
    """Budget summary narrative or tables."""
    prior_results: str = Field(default="", description="Previous results or track-record evidence relevant to the proposal.")
    """Previous results or track-record evidence relevant to the proposal."""
