# clothing_pro

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. Your solution must be a function deployed on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.

The project commited in the github have only the similarity search coding not Containerized using Docker due to compatible issues in the system.

API usage --

1. Start the server - 

```
uvicorn main:app --reload
```

2. Send a POST request to `http://localhost:8000/prediction` with the following JSON payload:

```
{
  "new_sentence": "joggers",
  "n": 2
}
```

3. The API will return a JSON response containing the predicted results:
```
{
  {
  "pred": [
    {
      "similarity": "0.45523083209991455",
      "URL": "https://www.flipkart.com/s-n-a-enterprises-jogger-fit-women-dark-blue-jeans/p/itm97d5a85f939c3?pid=JEAFWD2WHT9RTGQW&lid=LSTJEAFWD2WHT9RTGQW2ZZHJC&marketplace=FLIPKART&store=clo%2Fvua%2Fk58%2F4hp&srno=b_9_325&otracker=browse&fm=organic&iid=6f6c0eef-f11e-4eca-82b2-b1b5b473bedf.JEAFWD2WHT9RTGQW.SEARCH&ppt=None&ppn=None&ssid=16exc2b0000000001684822931978",
      "Name of the product": "women jogger fit mid rise dark blue jeans"
    },
    {
      "similarity": "0.44408196210861206",
      "URL": "https://www.flipkart.com/flying-girls-jogger-fit-women-blue-jeans/p/itmf9e0bb5b87354?pid=JEAFVXCZSEPBXGFV&lid=LSTJEAFVXCZSEPBXGFVHI493U&marketplace=FLIPKART&store=clo%2Fvua%2Fk58%2F4hp&srno=b_8_313&otracker=browse&fm=organic&iid=02471f8c-3d15-4a0f-9f2a-98283bcc028d.JEAFVXCZSEPBXGFV.SEARCH&ppt=None&ppn=None&ssid=bwueh2upo00000001684822930533",
      "Name of the product": "women jogger fit high rise blue jeans"
    }
  ]
}
```



