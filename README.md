# MusicPreprocessing
# Raga-Based Music Generation: Data Preprocessing Pipeline

In this research, we extend our previous work on Raga-based Machine Learning (ML) and focus on developing a robust data preprocessing pipeline to facilitate the development of future Raga music generation models. The unique and complex nature of Ragas in Indian music, characterized by their ability to evoke distinct emotions through specific note arrangements, necessitates specialized approaches in data preprocessing, which include melody extraction and Musical Instrument Digital Interface (MIDI) transcription.

## Overview

We present an end-to-end preprocessing pipeline aimed at supporting the generation models for traditional music forms like Raga, and in doing so, reviving the role of traditional music in modern composition. This pipeline is developed following an extensive review of 117 papers and meticulous implementation and evaluation of various techniques on real Raga music.

## Index Terms
- Deep Learning
- Raga-Based Music
- Traditional Indian Music
- Data Preprocessing pipeline
- Melody Extraction
- Midi Conversion
- Midi processing
- Raga Dataset
- ML Implementation
- Hybrid Demucs
- Basic-Pitch
- Music Generation
- Music Composition

## Methodology

The data preprocessing pipeline consists of six essential stages:
1. Conversion of raw files to wav or mp3 files.
2. Melody extraction.
3. MIDI conversion.
4. MIDI preprocessing, including track cleaning and segmentation.
5. Ascertainment of notes and variations as per Raga rules.
6. Music corrections, encompassing tempo, scale, and octave edits.

## Usage

### 1. Downloading Videos and Converting to Frames

```shell
!pip install -U yt-dlp
```
### 2. Extract Audio (mp3)
```shell
!pip install basic_pitch
```

### 3. Execute the following commands to download and convert YouTube playlists to mp3 format
```shell
!yt-dlp -x --audio-format mp3 -o "/path_to_save/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" <YouTube_playlist_link>
```

### 4. Processing MIDI Files
To process MIDI files, refer to the MidiPreprocessing.py file in the repository and execute it.
```shell
Python run MidiPreprocessing.py
```
### 5. Discussion and Results

In the course of this research, extensive experimentation with various models like NMF, Segnet, TONet, and Hybrid Demucs was carried out for extracting melodies, where the Hybrid Demucs model by Facebook proved to be the most suitable. For MIDI transcription, the Basic-Pitch model developed by Spotify Inc. was found to be most efficient.

### 6. Conclusion and Future Work

This project offers a scalable solution for developing high-quality datasets and preprocessing pipeline to revitalize traditional music forms like Raga and make them accessible to modern audiences. Future work will focus on developing a comprehensive model for generating Raga music, called ’Raga Multi-Track Music Machine’ (RMMM), and launching an open-source project for Raga MIDI generation.
