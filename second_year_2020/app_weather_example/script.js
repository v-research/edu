// Avvio geolocalizzazione
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (loc) {
            var lat = loc.coords.latitude;
            var lng = loc.coords.longitude;
            console.log(loc);
            initMap(lat, lng);
            document.getElementById('mapSearchDiv').style.display = 'block';
            document.getElementById('widgetDiv').style.display = 'block';
            weatherWidget(lat, lng);
        });
    }
}

// Creazione mappa
function initMap(lat, lng) {
    var myLatLng = {lat, lng};

    var mapProp = {
        center: new google.maps.LatLng(lat, lng),
        zoom: 10
    };
    document.getElementById('buttonDiv').remove();
    $('body').css('background-image', 'none');

    var map = new google.maps.Map(document.getElementById('map'), {
        center: new google.maps.LatLng(lat, lng),
        zoom: 15
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Ti trovi qui',
        draggable: true,
        animation: google.maps.Animation.DROP
    });

    var searchBox = new google.maps.places.SearchBox(document.getElementById('mapSearch'));

    google.maps.event.addListener(searchBox, 'places_changed', function () {
        var places = searchBox.getPlaces();
        var bounds = new google.maps.LatLngBounds();
        var i, place;

        for (i = 0; place = places[i]; i++) {
            bounds.extend(place.geometry.location);
            marker.setPosition(place.geometry.location);
        }
        ;
        map.fitBounds(bounds);
        map.setZoom(15);
        var lat = marker.getPosition().lat();
        var lng = marker.getPosition().lng();
        weatherWidget(lat, lng);
    });

    // Acquisizione coordinate marker dopo ogni spostamento
    google.maps.event.addListener(marker, 'dragend', function () {
        var lat = marker.getPosition().lat();
        var lng = marker.getPosition().lng();
        $('#lat').val(lat);
        $('#lng').val(lng);
        weatherWidget(lat, lng);
    });
}

// Richiesta dati meteo per widget
function weatherWidget(lat, lng) {
    var appId = '1b2b8bde5d366e86a2689499c5f69888';
    var temp = document.getElementById('temperature');
    var loc = document.getElementById('location');
    var icon = document.getElementById('icon');
    
    api_url = 'http://api.openweathermap.org/data/2.5/weather?lat=' +
            lat + '&lon=' + lng + '&units=metric&appid=' + appId + '&lang=it';
    $.ajax({
        url: api_url,
        method: 'GET',
        success: function (data) {
            icon.src = 'imgs/codes/' + data.weather[0].id + '.png';
            loc.innerHTML = data.name;
            temp.innerHTML = data.main.temp;
        }
    });
}