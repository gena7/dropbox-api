# Dropbox API Script

This simple script lets you export csv file with names and shared links of your files in dropbox.

## Usage

- Generate your access token on [Dropbox API](https://www.dropbox.com/developers)
  - Create Apps -> Login -> Choose DropboxAPI etc... -> Create App
  - Settings -> Generate access token

- Create `.env` file in the same directory as the current script and set your access token to `DB_ACCESS_TOKEN`.

```.env
DB_ACCESS_TOKEN='your_access_token'
```

- Also create `dropbox.csv` as empty file in the same directory.

- Run code

```python
python dropbox_api.py
```
