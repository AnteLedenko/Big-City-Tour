# Creating all necessary imports, creating a blueprint and three routes that  handle submitting review,
# editing review and deleting review. 
# All three routes require user to be authenticated in first route we have a function that gets tour id and review content
# from the form and then saves it with users id and redirects to city page. 
# In second route we have function that gets review id checks that the current user is owner of the review if edited commits new
# content to database and returns to next page (profile or city page). 
# And third route function just gets the review id makes sure current user owns the review and deletes the review
# commits change and redirect just like in previous route.

from flask import Blueprint, request, redirect, url_for ,render_template
from flask_login import current_user, login_required
from models import Review, db

reviews = Blueprint('reviews', __name__)

@reviews.route('/submit_review/<string:city>', methods=['POST'])
@login_required
def submit_review(city):
    tour_id = request.form.get("tour_id")
    review_content = request.form.get("review_content")

    if not tour_id or not review_content:
        return redirect(url_for(f'pages.{city}'))

    review = Review(
        user_id=current_user.user_id,
        tour_id=tour_id,
        review_content=review_content
    )
    db.session.add(review)
    db.session.commit()

    return redirect(url_for(f'pages.{city}'))

@reviews.route('/edit/<int:review_id>', methods=['GET', 'POST'])
@login_required
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)

    if review.user_id != current_user.user_id:
        return "Unauthorized", 403

    next_page = request.args.get('next') or url_for(f'pages.{review.tour.city.lower()}')

    if request.method == 'POST':
        new_content = request.form.get('review_content')
        if new_content:
            review.review_content = new_content
            db.session.commit()
            return redirect(next_page)

    return render_template('edit_review.html', review=review, next_page=next_page)

@reviews.route('/delete/<int:review_id>', methods=['POST'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)

    if review.user_id != current_user.user_id:
        return "Unauthorized", 403

    next_page = request.form.get('next') or url_for(f'pages.{review.tour.city.lower()}')

    db.session.delete(review)
    db.session.commit()
    return redirect(next_page)
