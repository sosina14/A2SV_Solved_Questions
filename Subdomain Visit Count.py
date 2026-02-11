class Solution(object):
    def subdomainVisits(self, cpdomains):
        counts = collections.defaultdict(int)

        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            fragments = domain.split('.')

            for i in range(len(fragments)):
                counts['.'.join(fragments[i:])] += count

        return [f"{count} {domain}" for domain, count in counts.items()]


        # result = []
        # for domain, count in counts.items():
        #     result.append(str(count) + " " + domain)

        # return result
