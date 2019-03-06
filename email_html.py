def email_content(twitter_info, podcast_info, fitness_info):

    email_body = f"""
        <html>
            <head>

               <title>Tutsplus Email Newsletter</title>
               <style type="text/css">
                a {{color: #d80a3e;}}
              body, #header h1, #header h2, p {{margin: 0; padding: 0;}}
              #main {{border: 1px solid #cfcece;}}
              img {{display: block;}}
              #top-message p, #bottom p {{color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }}
              #header h1 {{color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }}
              #header p {{color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }}
              h5 {{margin: 0 0 0.8em 0;}}
                h5 {{font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }}
              p {{font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}}
               </style>
            </head>
            <body>
            <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
            <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
                <tr>
                  <td align="center">
                  </td>
                </tr>
              </table>

            <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
                <tr>
                  <td>
                    <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
                      <tr>
                        <td width="570" align="center"  bgcolor="#008080"><h1>Daily Journal</h1></td>
                      </tr>
                      <tr>
                      </tr>
                    </table>
                  </td>
                </tr>


                <tr>
                  <td>
                    <div class="img-with-text" cellpadding="0" cellspacing="0" align="center">
                      <img src="https://images.unsplash.com/photo-1457433575995-8407028a9970?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=f83a8d50364692f9fd7b20b6342ac9aa&auto=format&fit=crop&w=2550&q=80" width="250" height="150"  />
                      <p>{twitter_info}</p>
                    </div>
                    <div class="img-with-text" cellpadding="0" cellspacing="0" align="center">
                      <img src="https://images.unsplash.com/photo-1526401485004-46910ecc8e51?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=126329be8d7b9c484ee5e2981fe1f907&auto=format&fit=crop&w=1500&q=80" width="250" height="150"  />
                      <p>{fitness_info}</p>
                    </div>
                    <div class="img-with-text" cellpadding="0" cellspacing="0" align="center">
                      <img src="https://images.unsplash.com/photo-1533612725328-d14882ad02ee?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7fbd8cfda16c68388cfc003304e86f27&auto=format&fit=crop&w=1300&q=80" width="250" height="150"  />
                      <p>{podcast_info}</p>
                    </div>
                  </td>
                </tr>

              </table>
              <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
              </table><!-- top message -->
            </td></tr></table><!-- wrapper -->

            </body>
            </html>
            """
    return email_body
