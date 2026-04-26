def test_unregister_success(client):
    """Test successful unregister from an activity."""
    # Arrange
    activity_name = "Soccer Team"
    email = "student@example.com"
    # First signup
    client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == f"Unregistered {email} from {activity_name}"


def test_unregister_not_registered(client):
    """Test unregister with email not registered."""
    # Arrange
    activity_name = "Soccer Team"
    email = "notregistered@example.com"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Student is not signed up for this activity"


def test_unregister_nonexistent_activity(client):
    """Test unregister from nonexistent activity."""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@example.com"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Activity not found"