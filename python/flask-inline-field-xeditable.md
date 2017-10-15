# Flask in-line field update with X-editable with CSRF
How to make in-line editable form fields with Flask and X-editable for bootstrap. While this example is based on bootstrap, [X-editable docs](https://vitalets.github.io/x-editable/docs.html) gives you an option of other libraries to chose from.

* Import libraries (Note to include x-editable after core library (bootstrap, jquery-ui)):
```html
<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">
<script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>

<link href="/static/new/bootstrap3-editable/css/bootstrap-editable.css" rel="stylesheet">
<script src="/static/new/bootstrap3-editable/js/bootstrap-editable.js"></script>
```

* Create an element that should be editable, add the field with csrf_token:
```html
<input name="_csrf_token" type="hidden" value="{{ csrf_token() }}">
<li><b>Phone number</b>: <a href="#" id="phone_number" data-pk="{{ user.id }}" data-type="number" data-url="{{ url_for('user_edit_phone') }}" data-title="Change your phone number">{{ user.phone_number }}</a></li>
```
Note that in this example, we use `phone_number` for id, we'll use that id, to apply editable to this element as a next step.

* Apply editable() method to this element, and add the token parameter to initalisation.
This will prevent our app from returning 403:
```html
<script>
$(document).ready(function() {
  $('#phone_number').editable({
    error: function (errors) {
    },
    params: function(params) {
        params["_csrf_token"] = $('[name="_csrf_token"]').val();
        return params;
    },
  });
});
</script>
```

* Now, below, we were calling the `user_edit_phone` url, here how it looks like in `views.py`
```python
@app.route('/user_edit_phone', methods=['GET', 'POST'])
def user_edit_phone():
    if request.method == 'POST':
        uid = request.form.get("pk")
        user = User.query.get(uid)
        user.phone_number = request.form.get("value")
        db.session.commit()
        return json.dumps({})
```

That should be it. For more about csrf with x-editable, you can check the this [issue](https://github.com/vitalets/x-editable/issues/741#issuecomment-91127543).
