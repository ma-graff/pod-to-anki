# Pod to Anki

## Summary

A tool designed for language learners to transcribe podcast audio, analyze word/phrase frequencies, and generate flashcards for Anki.

## Project Status

### Next Steps

The next steps for the project include:

1. **Finishing Base Features**:
    - Transcribe, rank (non-basic) words/phrases, generate TTS/fetch audio, convert to anki
2. **Implementing Anki Functionality**: Export to Anki easily.
3. **User Interface**: Develop a user-friendly interface for easier interaction with the tool. Possibly self-hosted, docker or just tkinter.
4. **Documentation**: Improve and expand the project documentation
5. **Extended Features** to be implemented later:
    - Create a better UI, host on some service.

## Tools Used

**Libraries:**
OpenAI Whisper (for transcription)
scikit-learn (for TF-IDF computation)
deep-translator (for translation)
pypandoc (for document conversion)
collections (native, for word frequency analysis)

Python 3.8+
```pip install whisper scikit-learn deep-translator pypandoc```
