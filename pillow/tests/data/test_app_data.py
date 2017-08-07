DATA = """
<!DOCTYPE html>
<html>
  <head lang="en">
    <meta charset="UTF-8">
    <title>Pillow</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- styles -->
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
  </head>
  <body>
    <div class="container">

      <h2>Pillow - Find your dream home.</h2>

      <div id="main">

        <form role="search" method="post" action="/searchHome" class="search-form">
            <div>
                <input name="address" maxlength="150" placeholder="Enter an address">
                <input name="citystatezip" maxlength="150" placeholder="Enter city, state or ZIP">
                <button type="submit">Search</button>
            </div>
        </form>



    <h3>Home Search Results</h3>

    <h4>Showing 1 results:</h4>
    <div id='results'>


        <div id='oneresult' style="margin: 40px 40px;">
            <div>2114 Bigelow Ave N, Seattle, WA 98109</div>
            <a href='http://www.zillow.com/homedetails/2114-Bigelow-Ave-N-Seattle-WA-98109/48749425_zpid/' target='_blank'>View Details</a>
            <div>Home Value</div>
            <div>Zestimate
                $2055778
                Last updated 08/06/2017
            </div>
            <div>Value Change
                by $68684
                last 30 days
            </div>
            <div>Valuation Range:
                low $1952989,
                high $2158567
            </div>

            <div>Neighborhood:
                <a href='http://www.zillow.com/local-info/WA-Seattle/East-Queen-Anne/r_271856/' target='_blank'>East Queen Anne</a>
            </div>
            <div>Median Zestimate $821,600</div>
        </div>


    </div>



      </div>
    </div>
    <!-- scripts -->
    <!--<script src="/static/scripts/js/main.js"></script>-->
  </body>
</html>
"""