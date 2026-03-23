def test_get_activities_returns_expected_structure(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    chess = payload["Chess Club"]
    assert set(chess.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(chess["participants"], list)


def test_get_activities_is_stable_across_calls(client):
    # Arrange
    url = "/activities"

    # Act
    first_response = client.get(url)
    second_response = client.get(url)

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.json() == second_response.json()
