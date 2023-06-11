from flask import Flask, request, render_template, redirect, abort
from pymongo import MongoClient
from bson import ObjectId
from analysis import get_polarity_scores
import math

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/reviews", methods=["GET", "POST"])
def reviews_fun():
    if request.method == "GET":
        reviews = reviews_collection.find()
        limit = 50
        page = 0
        if "limit" in request.args:
            limit = int(request.args["limit"])
        if "page" in request.args:
            page = int(request.args["page"]) - 1
        reviews = reviews.limit(limit).skip(page * limit)
        pages = math.ceil(reviews_collection.count_documents({}) / limit)
        return render_template(
            "reviews.html", reviews=reviews, page=page + 1, pages=pages
        )
    else:
        return "Create a review"


@app.route("/reviews/add", methods=["GET", "POST"])
def add_fun():
    if request.method == "GET":
        return render_template("add.html")
    else:
        reviews_collection.insert_one({"review": request.form["review"]})
        return redirect(f"http://localhost:5000/reviews")


@app.route("/reviews/edit/<string:review_id>", methods=["GET", "POST"])
def edit_fun(review_id):
    if request.method == "GET":
        review = reviews_collection.find_one({"_id": ObjectId(review_id)})
        return render_template("edit.html", review=review)
    else:
        reviews_collection.update_one(
            {"_id": ObjectId(review_id)},
            {"$set": {"review": request.form.get("review")}},
        )
        return redirect(f"http://localhost:5000/reviews")


@app.route("/reviews/<string:review_id>", methods=["GET", "DELETE"])
def review_fun(review_id):
    review_id = ObjectId(review_id)
    if request.method == "DELETE" or (
        "method" in request.args and request.args["method"] == "delete"
    ):
        reviews_collection.delete_one({"_id": review_id})
        return redirect(f"http://localhost:5000/reviews", code=302)
    elif request.method == "GET":
        review = reviews_collection.find_one({"_id": review_id})
        if review:
            return render_template(
                "review.html",
                review=review,
                score=get_polarity_scores(review["review"]),
            )
        abort(404)
    else:
        abort(400)


@app.route("/reviews/<string:review_id>/polarity", methods=["GET"])
def review_polarity(review_id):
    review_id = ObjectId(review_id)
    review = reviews_collection.find_one({"_id": review_id})
    if review:
        return get_polarity_scores(review["review"])
    abort(404)


@app.route("/", methods=["GET"])
def root_route():
    return redirect("/reviews")


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.SPLN
    reviews_collection = db.reviews
    app.run(debug=True)
