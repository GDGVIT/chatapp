# Project creation script
# (for Tornado on Heroku)
#
# by Shubham Bhardwaj
# --------------------------

# git!
git init

# --------------------------

# set up the pip requirements
touch requirements.txt
echo "Tornado==4.3" >> requirements.txt

# set up the Procfile
touch Procfile
echo "web: python server.py" >> Procfile

# --------------------------

echo "Committing to Git"

git add .
git commit -m "Initial Commit"

echo "Creating Heroku app & pushing"

heroku create --stack cedar
git push heroku master

echo "All Done!"
