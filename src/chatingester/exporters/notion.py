"""Notion exporter stub (no network calls yet)."""
from __future__ import annotations
2
from typing import List

from chatingester.exporters.base import Exporter
from chatingester.models.canonical import ConversationRecord


class NotionExporter(Exporter):
    name = "notion"

    def write(self, records: List[ConversationRecord], options: dict | None = None) -> None:
        options = options or {}
        dry_run = options.get("dry_run", True)
        if dry_run:
            return
        raise NotImplementedError("Notion exporter not implemented yet")
