string agreementUrl = MicrosoftAPIEndpoints.Endpoints.AgreementTemplatesDocument;
Console.WriteLine(agreementUrl); // Output: /v1/agreementTemplates/{templateId}/document

string loginUrl = string.Format(MicrosoftAPIEndpoints.AzureADLoginEndpoint, "yourCSPTenantID");
Console.WriteLine(loginUrl); // Output: https://login.microsoftonline.com/yourCSPTenantID/oauth2/token
