**Flow:**   
1. User goes to Site A (Client) 
2. User enters username and password 
3. Site A calls Site B (Server) resource /login which sets cookie in response 
4. Site A calls Site B resource /user which validates cookie sent in request and returns user details 
5. Site A displays user details 

**Sequence diagram:**  
Mermaid - [link](https://www.mermaidchart.com/app/projects/180edc5d-2f8c-4566-b6f8-7a699098920c/diagrams/5ac37870-04fb-41bf-bf8e-988bccc750c7/version/v0.1/edit) 


**Scenarios:**  
- TPC (third-party cookie) disabled [chrome incognito] 
- TPC enabled [chrome, firefox] 

**Results:** 
- TPC disabled - Doesn't work. Browser blocks both setting TPC by server as well as sending TPC to server. 
- TPC enabled - Works on both chrome and firefox.  
