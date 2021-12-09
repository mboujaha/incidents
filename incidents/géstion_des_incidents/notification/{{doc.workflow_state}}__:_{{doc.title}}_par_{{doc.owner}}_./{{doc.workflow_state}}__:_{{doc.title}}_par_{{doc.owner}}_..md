<table class="panel-header" border="0" cellpadding="0" cellspacing="0" width="100%">
    <tr height="10"></tr>
    <tr>
        <td width="15"></td>
        <td>
            <div class="text-medium text-muted">
                <span>{{_("Incident :")}} {{ doc.title }}</span>
            </div>
        </td>
        <td width="15"></td>
    </tr>
    <tr height="10"></tr>
</table>

<table class="panel-body" border="0" cellpadding="0" cellspacing="0" width="100%">
    <tr height="10"></tr>
    <tr>
        <td width="15"></td>
        <td>
            <div>
                {{ doc.description }}
                <ul class="list-unstyled" style="line-height: 1.7">
                    <li>{{_("Qualification ")}}: <b>{{ doc.qualification }}</b></li>
                    <li>{{_("Catégorie ")}}: <b>{{ doc.incident_cat }}</b></li>
                    <li>{{_("Sous-Catégorie ")}}: <b>{{ doc.incident_sub_cat }}</b></li>
                    {% set date_dec = frappe.utils.get_datetime(doc.incident_date) %}
                    <li>{{_("Date de déclaration")}}: <b>{{ date_dec.strftime("%A, %d %b %Y at %I:%M %p") }}</b>
                    </li>
                    <li>{{ _('Incident Link') }}: {{ frappe.utils.get_link_to_form(doc.doctype, doc.name) }}</li>
                </ul>
            </div>
        </td>
        <td width="15"></td>
    </tr>
    <tr height="10"></tr>
</table>
