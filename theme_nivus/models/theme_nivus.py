from odoo import models


class ThemeNivus(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_nivus_post_copy(self, mod):
        self.enable_view('website.template_footer_descriptive')
