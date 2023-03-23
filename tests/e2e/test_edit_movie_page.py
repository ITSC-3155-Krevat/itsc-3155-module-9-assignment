# TODO: Feature 5
from src.repositories.movie_repository import get_movie_repository

def test_edit_movie_page(test_app):
    movie_repository = get_movie_repository()
    examplemovie = movie_repository.create_movie('Harry Potter: The Chamber of Secrets', 'Davis Yates', 3)
    movie_repository._db[0] = examplemovie
# Checking the response within the database in the first array with the movie filler.
    response = test_app.get('/movies/0/edit')
    data = response.data.decode('utf-8')

    assert response.status_code == 200

    assert '''  <label for="title">Title</label>
  <input type="text" class="form-control" id="title" name="title" value='Harry Potter: The Chamber of Secrets' required>
  <br>
  <label for="director">Director</label>
  <input type="text" class="form-control" id="director" name="director" value='Davis Yates' required>
  <br>
  <label for="rating">Rating</label> 
  <select class="form-control" id="rating" name="rating" required>
    <option value="1" >1</option>
    <option value="2" >2</option>
    <option value="3" >3</option>
    <option value="4" >4</option>
    <option value="5" selected>5</option>
  </select>
  <br>
  <button type="submit" class="btn btn-primary">Save</button>
</form>  ''' in data
