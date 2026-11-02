#Voice-Controlled 2D Navigation System (Cognitive Robotics)

A Python-based prototype integrating Speech-to-Text (ASR), intent parsing, and autonomous 2D grid navigation. Developed as a preliminary framework for LLM-driven human-robot interaction (HRI) research.

## Features
- **Perception:** Captures audio input via microphone using `sounddevice` and processes it through ASR.
- **Parsing:** Translates spoken directional commands into coordinate targets.
- **Navigation Control:** Executes step-by-step spatial movement across a 2D grid matrix.

## Requirements
- Python 3.x
- `speech_recognition`
- `sounddevice`
- `numpy`
- `scipy`
