To contribute to `revenuecat_python`, follow these steps for local development:

1. Fork the `revenuecat_python` repo on GitHub.

   ```
   $ git clone https://github.com/yuriihavrylko/revenuecat_python.git
   ```

2. Install your local copy into a virtualenv. If you have virtualenvwrapper installed, do the following:

   ```
   $ mkvirtualenv revenuecat_python
   $ cd revenuecat_python/
   $ python setup.py develop
   ```

3. Create a branch for local development:

   ```
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

   Now you can make your changes locally.

4. Commit your changes and push your branch to GitHub:

   ```
   $ git add .
   $ git commit -m "Your detailed description of your changes."
   $ git push origin name-of-your-bugfix-or-feature
   ```

5. Submit a pull request through the GitHub website.
