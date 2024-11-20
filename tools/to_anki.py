# Sample with csv

from anki.collection import ImportCsvRequest
from aqt import mw
col = mw.col
path = "/home/dae/foo.csv"

metadata = col.get_csv_metadata(path=path, delimiter=None)
request = ImportCsvRequest(path=path, metadata=metadata)
response = col.import_csv(request)

print(response.log.found_notes, list(response.log.updated), list(response.log.new))