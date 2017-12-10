// function to generate an unique identifier
function generateUUID() {
    "Function for generating unique identifiers"
    var d = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    return uuid;
};

// function to set contact UUID
function setContactUUID() {
    if (sessionStorage.getItem('uuid') == null) {
        sessionStorage.setItem('uuid', generateUUID());
    }
}

// function to set contact ID
function setContactID(contact_id) {
    if (sessionStorage.getItem('contact_id') == null) {
        sessionStorage.setItem('contact_id', contact_id);
    }
}

// function to add a web page access (url and date)
function setPageAccess() {
    // date and time
    var today = new Date();
    var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var dateTime = date + ' ' + time;

    if (sessionStorage.getItem('contact_id') == null) {
        if (sessionStorage.getItem('urls') == null) {
            sessionStorage.setItem('urls', window.location.href);
            sessionStorage.setItem('dates', dateTime);
        } else {
            sessionStorage.setItem('urls', sessionStorage.getItem('urls') + ',' + window.location.href);
            sessionStorage.setItem('dates', sessionStorage.getItem('dates') + ',' + dateTime);
        }
    } else {
        sessionStorage.setItem('urls', window.location.href);
        sessionStorage.setItem('dates', dateTime);
        sendPageRequest();
    }
}

// function to update sessionStorage
function updateSessionStorage() {
    setContactUUID();
    setPageAccess();
}

// post to URL
function post_to_url(path, params, method) {
    method = method || "post";

    var form = document.createElement("form");

    //Move the submit function to another variable
    //so that it doesn't get overwritten.
    form._submit_function_ = form.submit;

    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for (var key in params) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
    }

    document.body.appendChild(form);

    // clear current session
    sessionStorage.removeItem('urls');
    sessionStorage.removeItem('dates');

    form._submit_function_(); //Call the renamed function.
}

// function contact send request to our application
function sendContactRequest() {
    post_to_url('http://localhost:5000/add/contact',
        {
            'email': document.getElementById('email').value,
            'name': document.getElementById('name').value,
            'urls': sessionStorage.getItem('urls').split(','),
            'dates': sessionStorage.getItem('dates').split(','),
        });
}

// function page send request to our application
function sendPageRequest() {
    post_to_url('http://localhost:5000/add/page',
        {
            'contact_id': sessionStorage.getItem('contact_id'),
            'url': sessionStorage.getItem('urls'),
            'date': sessionStorage.getItem('dates')
        });
    resetUpdate();
}