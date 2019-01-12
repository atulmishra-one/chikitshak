window.addEventListener('load', function () {
    var countryControlApp = new Vue({
        el: "#id_country",
        mounted: function(){
            var vm = this;
            jQuery("#id_country").change(function(e){
                stateControlApp.getStates(this.value);
            });
        },
    });

    var stateControlApp = new Vue({
        delimiters: ["[[", "]]"],
        el: "#id_state",
        data: {
            states: []
        },
        mounted: function(){
            jQuery("#id_state").change(function(e){
                axios.get("/location/api/city/?format=json&state_id="+this.value).then(function(response){
                    var options = "";
                    jQuery.each(response.data, function(i, row){
                        options += "<option value="+row.id+">"+row.name+"</option>"
                    });
                    jQuery("#id_city").empty().html(options);
                });
            });
            if( jQuery("#id_country").val() ){
                this.getStates(jQuery("#id_country").val());
            }
        },
        methods: {
            getStates: function(countryID){
                var vm = this;
                axios.get("/location/api/state/?format=json&country_id="+countryID).then(function(response){
                    vm.states = response.data;
                });
            },
        }
    });
});
