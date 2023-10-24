# Dependable Attributes

## Maintainability

The system is modular and all classes are broken up. Adding attributes to a specific object is as easy as changing the single class. The database is independent of the website such that a mobile application could be built with the same backend.

## Error Tolerance

Dropdown menus are the only way to select information that is sensitive to error. This ensures that people cannot input the incorrect information whenever they try to log in. Errors are thrown when there is invalid patient information given and there is no exploitation in the code. The only form that the patient could mess up is their name which is a simple string value. Since they are string values, injection is unlikely.

## Availability

The website can be deployed on multiple servers in order to maximize the uptime. The main domain that we provide as the landing page will discretely point to one of the sub servers running the program in order to maintain its dependability. The uptime is then maximized.