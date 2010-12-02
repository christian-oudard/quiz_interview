documents = {
    1: {'status': 'Draft', 'parent': None},
    2: {'status': 'Old', 'parent': None},
    3: {'status': 'Active', 'parent': 2},
    4: {'status': 'Draft', 'parent': 3},
    5: {'status': 'Deleted', 'parent': 3},
    6: {'status': 'Deleted', 'parent': 2},
}

def get_lineage(id, documents):
    """
    >>> get_lineage(1, documents)
    [1]
    >>> get_lineage(5, documents)
    []
    >>> get_lineage(4, documents)
    [2, 3, 4]
    >>> get_lineage(3, documents)
    [2, 3, 4]
    """
    if documents[id]['status'] == 'Deleted':
        return []

    def parent(id):
        return documents[id]['parent']

    def child(parent_id):
        for id, doc in documents.items():
            if doc['parent'] == parent_id and doc['status'] != 'Deleted':
                return id
        return None

    # find the root of the lineage
    root_id = id
    while True:
        p = parent(root_id)
        if p is None:
            break
        root_id = p

    # get the descendants
    lineage = []
    doc_id = root_id
    while doc_id:
        lineage.append(doc_id)
        doc_id = child(doc_id)

    return lineage

import doctest
doctest.testmod(verbose=True)
