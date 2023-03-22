from app import app
# TODO: Feature 1
def test_all_movies():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert response.status_code == 200


    response = test_app.post('/movies', data={
    'dir': 'Steven',
    'mname': 'Testmovie1',
    'rating': "3"
    }, follow_redirects=True)
    response = test_app.get("/movies")
    data = response.data.decode('utf-8')
    assert response.status_code == 200
    dict = []

    dict.append(data)
    assert response.status_code == 200
    assert '<td scope="row" class="table-success">Steven</td>' in data
    assert '<td scope="row" class="table-success">Testmovie1</td>' in data
    assert '<td scope="row" class="table-success">3</td>' in data
    assert '<td scope="row" class="table-success">steven</td>' not in data
    assert '<td scope="row" class="table-success">testmovie1</td>' not in data
    assert '<td scope="row" class="table-success">33</td>' not in data
    
    # assert dict.get
    

