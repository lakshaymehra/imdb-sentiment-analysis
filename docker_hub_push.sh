
docker login

# docker tag image_name user_name/repo_name:image_name

docker tag sentiment_analysis_api lm3899/imdb-reviews-sentiment-analysis:sentiment_analysis_api

docker push sentiment_analysis_api