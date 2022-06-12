# host-heroku-bot

<h1><b>Prerequisites For Development</b></h1>

<ul>
<li>Python 2.6 or greater.</li>

<li>Pip package management tool to download dependencies.</li>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="pip install -r requirements.txt"><pre class="notranslate"><code>pip install -r requirements.txt
</code></pre></div>
  
<li>Get API credentials from Stocktwits.</li>

</ul>

<h1><b>Production</b></h1>
1. Remove any static API credentials and place them in Heroku server settings.
<br>
2. Follow https://devcenter.heroku.com/articles/git to deploy application to Heroku via git.

<h1><b>stwits.py</b></h1>
Application will automatically post messages and images to Stocktwits based on given time and day.
<br>
Refer to https://api.stocktwits.com/developers for more documentation.
