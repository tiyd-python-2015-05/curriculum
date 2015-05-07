from pig_latin import pig_latin


def test_simple_words():
    assert pig_latin("pig") == "igpay"
    assert pig_latin("diorama") == "ioramaday"


def test_consonant_clusters():
    assert pig_latin("glove") == "oveglay"
    assert pig_latin("strawberry") == "awberrystray"


def test_beginning_vowel():
    assert pig_latin("egg") == "eggway"
    assert pig_latin("icicle") == "icicleway"


def test_phrases():
    assert pig_latin("eight nights of horror") == \
        "eightway ightsnay ofway orrorhay"


def test_sentences():
    assert pig_latin("How can a gentle beast live in this savage world?") == \
        ("Owhay ancay away entlegay eastbay ivelay inway isthay avagesay "
         "orldway?")
    assert pig_latin("In the sunshine, all nightmares melt.") == \
        "Inway ethay unshinesay, allway ightmaresnay eltmay."
