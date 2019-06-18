
class ProjectHelper:

    def __init__(self,app):
        self.app = app

    def create_new_project(self,project):
        self.click_manage()
        self.click_manage_project()
        self.click_create_new_project()
        self.fill_project(project)
        self.click_add_project()

    def delete_project_by_id(self,id):
        self.click_manage()
        self.click_manage_project()
        self.open_project_by_id(id)
        self.click_delete_project()
        self.click_delete_project()

    def fill_project(self,project):
       self.set_text_field("name",project.name)
       self.set_select_field("status",project.status)
       self.set_checkbox("inherit_global",project.inhert)
       self.set_select_field("view_state",project.view_status)
       self.set_text_field("description", project.description)

    def click_manage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def open_project_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def click_manage_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def click_delete_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def click_create_new_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Create New Project']").click()

    def click_add_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def set_text_field(self, field_name, text):
        wd = self.app.wd

        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def set_select_field(self, field_name, select):
        wd = self.app.wd

        if select is not None:
            wd.find_element_by_css_selector("select[name='%s']" % field_name).click()
            wd.find_element_by_css_selector("option[value='%s']" % select.value).click()

    def set_checkbox(self,field_name, val):
        wd = self.app.wd

        if val is False:
            wd.find_element_by_css_selector("input[name='%s']" % field_name).click()