# Copyright 2017 Smartwaiver
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import smartwaiver

# The API Key for your account
api_key = '[INSERT API KEY]'

template_id = '[INSERT TEMPLATE ID]'

# Set up your Smartwaiver connection using your API Key
sw = smartwaiver.Smartwaiver(api_key)

# Retrieve a specific template (SmartwaiverTemplate object)
template = sw.get_waiver_template(template_id)

# Access properties of the template
# These are all the available properties for a SmartwaiverTemplate
print('Template ID: ' + template.template_id)
print('Title: ' + template.title)
print('Published On: ' + template.published_on)
print('Published Version: ' + str(template.published_version))
print('Web URL: ' + template.web_url)
print('Kiosk URL: ' + template.kiosk_url)

