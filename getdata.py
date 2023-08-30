# ! /pyscript python
def fragment(pkt,fragsize=1480):
	fragsize=(fragsize + 7)//8*8
	lst=[]
	for p in pkt:
		s=raw(p[IP].payload)
		nb=(len(s)+fragsize-1)//fragsize
		for i in range(nb):
			q=p.copy()
			del(q[IP].payload)
			del(q[IP].chksum)
			del(q[IP].len)
			if i != nb-1 :
				q[IP].flags |= 1
			q[IP].frag+=i*fragsize // 8
			r=conf.raw_layer(load=s[i*fragsize:(i+1)*fragsize])
			r.overload_fields = p[IP].payload.overload_fields.copy()
			q.add_payload(r)
			lst.append(q)
	return lst
