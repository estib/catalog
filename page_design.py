__author__ = 'Steve'
# This file contains all the functions and variables used to create the html
# content of the catalog app. It's all written to be fed into flask.


def make_category_content(categories, user_string):
    # this function makes the html for the category list of the catalog app.
    # it only adds add/delete functionality if user_string is not empty.
    content = '''
    <table style="width: 100%;"><tr>
    <td width="33%;" style="vertical-align: top;">
    <div style="float: left;"><h3>Categories:</h3>
    '''
    if categories == []:
        content += 'There are no categories.'
    else:
        for cat in categories:
            content += '''<div>%s
            <form action="/catalog" method="POST">
            <input type="submit" name="catsel_%s_" id="catsel" value="Select">
            ''' % (cat[1], cat[0],)
            # only add delete button if the user created the category
            if cat[2] == user_string:
                content += '''
                <input type="submit" name="catdel_%s_" id="catdel" value="Delete" onclick="return confirm('Do you really want to delete this category?');">
                ''' % (cat[0],)
            content += '</form></div>'
    # only let users add categories if they are logged in.
    if user_string != '':
        content += """
            <div>
                <form action="/catalog" method="POST">
                    <h4>Add a Category:</h4>
                    <input type="text" name="new_category" id="ncat" placeholder="Category Name">
                    <input type="submit" name="newcat" id="ncatsub" value="Add Category">
                </form>
            </div>
        """
    content += '</div></td>'
    return content


def make_item_content(cat_name, it_list, cat_id, user_string):
    # this function makes the html for the item list of the catalog app.
    # it only adds add/delete functionality if user_string is not empty.
    content = str(
        '<td width="33%%;" style="vertical-align: top; border-left: 1px solid #2E3136;">' +
        '<div style="float: left; margin-left: 15px"><h3>Category: %s</h3>'
        % (cat_name,)
    )
    if it_list[0] is None:
        content += 'There are no items in this category.'
    else:
        for it in it_list:
            content += '''<div>%s
            <form action="/catalog" method="POST">
            <input type="submit" name="itsel_%s-from-%s_" id="itsel" value="Select">
            ''' % (it[1], it[0], cat_id)
            # Only add delete button if user is the creator of the item
            if it[2] == user_string:
                content += '''
                <input type="submit" name="itdel_%s-from-%s_" id="itdel" value="Delete" onclick="return confirm('Do you really want to delete this item?');">
                ''' % (it[0], cat_id)
            content += '</form></div>'
    # Only let user add item if user is logged in
    if user_string != '':
            content += """
            <div>
                <form action="/catalog" method="POST">
                    <h4>Add an Item to this Category:</h4>
                    <input type="text" name="new_item" id="nit" placeholder="Item Name">
                    <br/><br/>
                    <textarea name="new_item_desc" rows="7" cols="50" placeholder="Describe the item here."></textarea>
                    <br/><br/>
                    <input type="url" name="new_pic" id="npic" placeholder="Picture Url">
                    <br/><br/>
                    <input type="submit" name="newit_%s_" id="newit" value="Add Item">
                </form>
            </div>
            """ % (cat_id,)
    content += '</div></td>'
    return content


def make_description(it_id, it_stuff, cat_id, to_edit, cat_list, user_string):
    # this function makes the html for the category list of the catalog app.
    # it only adds edit functionality if user_string is not empty.
    text = it_stuff[1]
    it_name = it_stuff[0]
    it_creator_id = it_stuff[3]
    it_pic = it_stuff[4]
    if it_pic is None:
        it_pic = ''
    if to_edit is False:
        content = """
        <td width="33%%" style="vertical-align: top; border-left: 1px solid #2E3136;">
        <div style="float: left; margin-left: 15px">
        <h3>%s</h3>
        <h4>Description:</h4>
        <p>%s</p>
        <h4>Picture</h4>
        """ % (it_name, text)
        if it_pic == "":
            content += '<p>There is no picture for this item.</p>'
        else:
            content += '<img src="%s" height="75" width="75"><br/><br/>' % it_pic
        if user_string == it_creator_id:
            content += """
            <form action="/catalog" method="POST">
            <input type="submit" name="ited_%s-from-%s_" id="ited" value="Edit">
            </form>
            """ % (it_id, cat_id)
        content += '</div><td>'
    elif to_edit is True:
        content = """
        <td width="33%%" style="vertical-align: top; border-left: 1px solid #2E3136;">
        <div style="float: left; margin-left: 15px">
        <form action="/catalog" method="POST">
        <h3>Edit</h3>
        <input type="text" name="it_name" id="it_n_edit" value="%s">
        <h4>Description:</h4>
        <textarea name="desc_edit" rows="7" cols="50">%s</textarea><br/>
        <br/>
        <h4>Picture:</h4>
        <input type="url" name="pic_edit" id="edit_pic" value="%s" placeholder="Picture Url">
        <br/><br/>
        """ % (it_name, text, it_pic)
        content += make_cat_edit_list(cat_list, cat_id, user_string)
        content += '''
        <input type="submit" name="nited_%s-from-%s_" id="nited" value="Submit Edit">
        </form></div></td>
        ''' % (it_id, cat_id)
    return content


def make_cat_edit_list(cats, cat_id, user_string):
    # this adds the 'category edit' list to the description editor. it only
    # includes in the list those categories that the user created.
    content = '<br/><select name="cat_edit">'
    for cat in cats:
        if str(cat[0]) == str(cat_id):
            content += str('<option selected="selected" value="%s">%s</option>'
                           % (cat[0], cat[1]))
        elif str(cat[2]) == user_string:
            content += '<option value="%s">%s</option>' % (cat[0], cat[1])
    content += '</select><br/><br/>'

    return content


def make_saved_item(it_name):
    # this makes the confirmation html for when an item is edited.
    content = '''
        <td width="33%%" style="vertical-align: top; border-left: 1px solid #2E3136;">
        <div style="float: left; margin-left: 15px">
        <h3>%s Saved</h3>
        </div></td>
    ''' % (it_name,)
    return content


def make_page_header(user_string):
    # this makes the header html for all the pages of the catalog app.
    # it changes the login/logout link depending on the user's login status.
    content = '''
    <head>
    <meta charset="utf-8">
    <title>Catalog of Stuff</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='catalog.css') }}" />
    <header>
        <div class="container">
        <a href="/catalog"><h1 class="logo">Category of Stuff</h1></a>
        </div>
        <div class="container">
        <strong><nav>
            <ul class="menu">
    '''
    if user_string == '':
        content += '<a href="/catalog/login"><h2 class="logo">Login<h2></a>'
    else:
        content += '<a href="/catalog/logout"><h2 class="logo">Logout<h2></a>'
    content += '''
            </ul>
            <ul class="menu">
            <h2>|</h2>
            </ul>
            <ul class="menu">
            <a href="/catalog/json"><h2 class="logo">Get JSON</h2></a>
            </ul>
        </nav></strong>
        </div>
    </header>
    </head>
    '''
    return content

# includes JS content to handle google plus sign-in
login_content = '''
    <html>
    <meta charset="utf-8">
    <title>Catalog of Stuff</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='catalog.css') }}" />
    <header>
        <div class="container">
        <a href="/catalog"><h1 class="logo">Category of Stuff</h1></a>
        </div>
        <div class="container">
        <strong><nav>
            <ul class="menu">
            <a href="/catalog/login"><h2 class="logo">Login<h2></a>
            </ul>
            <ul class="menu">
            <h2>|</h2>
            </ul>
            <ul class="menu">
            <a href="/catalog/json"><h2 class="logo">Get JSON</h2></a>
            </ul>
        </nav></strong>
        </div>
    </header>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
        </script>
        <script src="https://apis.google.com/js/client:platform.js?onload=start" async defer>
        </script>
    </head>

    <body>
        <table style="horizontal-alignment: center; width: 100%;"><tr><td align="center">
        <div style="horizontal-alignment: center">
        <h3>Sign in with Google Plus:</h3></div>
        <div id="signinButton">
            <span class="g-signin"
                data-scope="openid"
                data-clientid="324284088553-dsp0p7ano5tkgp1m50bfnmfnnjd4877a.apps.googleusercontent.com"
                data-redirecturi="postmessage"
                data-accesstype="offline"
                data-cookiepolicy="single_host_origin"
                data-callback="signInCallback"
                data-approvalprompt="force">
            </span>
        </div>
    <div id="result"></div>
    </td></tr></table>

    <script>
    function signInCallback(authResult) {
        if (authResult['code']) {
            // hide the signin button
            $('#signinButton').attr('style', 'display: none');
            // send one-time-use code to server
            $.ajax({
                type: 'POST',
                url: '/gconnect?state={{ STATE }}',
                processData: false,
                contentType: 'application/octet-stream; charset=utf-8',
                data: authResult['code'],
                success: function (result) {
                    if (result) {
                        $('#result').html('Login Successful!</br>' + result + '</br>Redirecting...')
                        setTimeout(function() {
                            window.location.href = "/catalog";
                        }, 3000);
                    } else if (authResult['error']) {
                        console.log('Error: ' + authResult['error']);
                    } else {
                        $('result').html('Failed to make a server-side call. Maybe check your configuration and console.');
                    }
                }
            });
        }
    }
    </script>

    </body>

    </html>
'''
