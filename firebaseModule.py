def agregar(db, coll, dictData, doc = False):
    if not doc:
        doc_ref = db.collection(coll).document()
        doc_ref.set(dictData)
    else:
        doc_ref = db.collection(coll).document(doc)
        doc_ref.set(dictData)
