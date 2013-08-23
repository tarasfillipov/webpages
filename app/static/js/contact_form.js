jQuery(function() {
    var form = jQuery("#UserInfoForm");
    form.submit(function(e) {
        jQuery("#id_send").attr('disabled', true)
        //form.find(':input:not(:disabled)').prop('disabled',true)

        jQuery("#sendmessage").prepend('<span>Saving changes, please wait</span>')
        jQuery("#ajaxwrapper").load(
            form.attr('action') + ' #ajaxwrapper',
            form.serializeArray(),
            function(responseText, responseStatus) {
                jQuery("#id_send").attr('disabled', false)
                if (responseText == 'success'){

                    window.location = '/'
                }
            }
        );
        e.preventDefault();
    });
});