# NeuraVis
The project aims to utilize Electroencephalography (EEG) to monitor, analyze, and interpret brainwave activity for applications in neuroscience, mental health, and human-computer interaction. 
# Hardware indeed
1. Elecrodes
  -Dry Electrodes: Easier to use, no gel needed, but less sensitive.
  -Wet Electrodes: Require conductive gel, generally more accurate.
  -Flexible/Cap Arrays: For multi-channel setups, pre-arranged caps can simplify the process.
3. Amplifiers
  -EEG signals are very weak (~μV range). You'll need high-gain, low-noise amplifiers to boost the signal.
  -Instrumentation Amplifiers like the INA114 or AD620 are common choices.
4. Filters
  -To remove noise (e.g., 50/60 Hz power line interference), you'll need bandpass filters to isolate the EEG frequency bands:
  -Delta (0.5–4 Hz)
  -Theta (4–8 Hz)
  -Alpha (8–13 Hz)
  -Beta (13–30 Hz)
  -Active or passive filtering circuits can be used.
5. Analog-to-Digital Converter (ADC)
  -EEG signals are analog, so you'll need an ADC to convert them into digital form for processing.
  -Choose a high-resolution ADC (e.g., 16-bit or 24-bit) for better accuracy.
6. Microcontroller or Single-Board Computer
  -To process the digital signals, you can use:
  -Arduino: For simple systems.
  -Raspberry Pi: For more processing power and advanced applications.
  -STM32 or ESP32: For embedded systems.
7. Power Supply
  -Use a clean, stable power source to avoid introducing noise into the system.
  -Battery-powered setups are common for portability and reduced electrical interference.
