#!/usr/bin/env python3
"""
Nebula AI Toolkit
Open-source AI utilities for creators.
"""

import argparse

PROMPTS = {
    "script": (
        "Write an engaging YouTube script about: {topic}. "
        "Use a strong hook, natural narration, and a clear structure."
    ),
    "title": (
        "Generate 10 clickable but honest YouTube titles about: {topic}. "
        "Avoid misleading clickbait."
    ),
    "description": (
        "Write an SEO-friendly YouTube description about: {topic}. "
        "Include relevant keywords and natural hashtags."
    ),
    "thumbnail": (
        "Create a detailed cinematic YouTube thumbnail concept about: {topic}. "
        "Describe composition, lighting, subject, and text."
    ),
}


def generate_prompt(mode: str, topic: str) -> str:
    """Generate a creator-focused AI prompt."""
    if mode not in PROMPTS:
        raise ValueError(f"Unsupported mode: {mode}")

    return PROMPTS[mode].format(topic=topic)


def main():
    parser = argparse.ArgumentParser(
        description="Nebula AI Toolkit - Creator Prompt Generator"
    )

    parser.add_argument(
        "mode",
        choices=PROMPTS.keys(),
        help="Choose a prompt type",
    )

    parser.add_argument(
        "topic",
        help="Your video topic",
    )

    args = parser.parse_args()

    print("\n--- NEBULA AI TOOLKIT ---\n")
    print(generate_prompt(args.mode, args.topic))
    print("\n------------------------")


if name == "main":
    main()
