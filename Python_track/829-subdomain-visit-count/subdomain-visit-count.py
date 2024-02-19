class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # create dictionary to count the domains and list to return the result
        sub_domain_count = {}
        result = []

        # loops through the domains and perform finding the subdomains and updating the dictionary with the result
        for domains in cpdomains:

            # splitting the domains
            counter, domain = domains.split()
            counter = int(counter)
            subdomains = domain.split(".")

            # looping through the subdomains and updatingg the count of the dictionary with their result
            for i in range(len(subdomains)):
                dm = subdomains[i]
                for j in range(i+1, len(subdomains)):         
                    dm = dm + "." + subdomains[j]
                sub_domain_count[dm] = sub_domain_count.get(dm, 0) + counter

        # looping through the dictionary and appending the result to the result list in with the required format
        for domain in sub_domain_count:
            result.append(str(sub_domain_count[domain]) + " " + domain)

        return result