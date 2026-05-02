def test_signup_success(client):
    """Test successful signup for an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "student@example.com"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == f"Signed up {email} for {activity_name}"


def test_signup_duplicate(client):
    """Test signup with already registered email."""
    # Arrange
    activity_name = "Chess Club"
    email = "duplicate@example.com"
    # First signup
    client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Act - second signup
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Student already signed up for this activity"


def test_signup_nonexistent_activity(client):
    """Test signup for nonexistent activity."""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@example.com"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Activity not found"