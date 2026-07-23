"""Lightweight ML classifier for routing """

from backend.models import RouteDecision


def route_by_classifier(prompt: str) -> RouteDecision:
    raise NotImplementedError()
