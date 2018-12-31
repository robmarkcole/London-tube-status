"""
Test london_tube_stats with pytest.
"""
import london_tube_status as lts
import requests_mock
import json

VALID_RESPONSE = [
    {
        "name": "Bakerloo",
        "lineStatuses": [{"statusSeverityDescription": "Good Service"}],
    },
    {
        "name": "London Overground",
        "lineStatuses": [
            {"statusSeverityDescription": "Minor Delays", "reason": "Something"}
        ],
    },
]


def test_tube_data():
    """Test TubeData."""
    with requests_mock.Mocker() as mock_req:
        url = lts.API_URL
        mock_req.get(url, text=json.dumps(VALID_RESPONSE))
        test_tube_data = lts.TubeData()
        test_tube_data.update()
        assert test_tube_data.data["Bakerloo"] == {
            "Description": "Nothing to report",
            "State": "Good Service",
        }
        assert test_tube_data.data["London Overground"] == {
            "Description": "Something",
            "State": "Minor Delays",
        }
