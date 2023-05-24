def agregar(db, coll, dictData, doc = False):
    if not doc:
        doc_ref = db.collection(coll).document()
    else:
        doc_ref = db.collection(coll).document(doc)
    doc_ref.set(dictData)

def updt(db, coll, dictData, doc):
    doc_ref = db.collection(coll).document(doc)
    city_ref.update(dictData)

def read(db, coll, doc = False):
    if not doc:
        users_ref = db.collection(coll)
        docs = users_ref.stream()
        reader = []
        for doc in docs:
            reader.append(doc.to_dict())
    else:
        doc_ref = db.collection(coll).document(doc)
        doc = doc_ref.get()
        reader = doc.to_dict()
    
    return reader
