# Fetch Rewards Coding Challenge

## Configuration

The purpose of this challenge was to design and build an API that could handle two endpoints: `process_receipts` and `get_points`. 

This applet was build using python, with flask being the chosen backend framework. Docker was used to containerize the applet. To run it, from the project root directory simply run:

```
docker compose --build
```

This will both build the docker image and run the container. This API will be mapped to localhost port `5000`.

Postman was used to test and verify that the API endpoints work. Some sample endpoints being:

### Process Receipts
```
http://127.0.0.1:5000/receipts/process
```

Which resulted in the following JSON object:
```
{
    "id": "9caeded5-4b08-4eae-a41d-4fef88387de3"
}
```

### Get Points
```
http://127.0.0.1:5000/receipts/9caeded5-4b08-4eae-a41d-4fef88387de3/points
```

Which resulted in the following JSON object:
```
{
    "points": 109
}
```

## Design Choices

Two separate objects were created for `Receipt` and `Item`. Getters and setters were created for both, the getters for `Receipt` in particular were of use when calculating points.

If a JSON object had a missing field, i.e. `total`, then the a `400` error would be thrown since all fields are used for the calculation of the points. An alternate design would have been to not calculate points for a field that was missing, i.e. if `retailer` was empty, we simply skip that calculation.