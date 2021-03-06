import email

##########

##########

# Attributes:
#	message:	the thread parsed into email.message format
#	messageID:	the thread's message number or message-ID
#	newsgroup:	the newsgroup object, wrapper for calls to nntplib
	
class SinglePost:
	
	#####

	def __init__(self, messageID, newsgroup):
		self.messageID = messageID
		self.newsgroup = newsgroup
		
                # the body() method returns tuple (response, info), where info is a namedtuple (number, message_id, lines[])
#		header = self.newsgroup.head(self.messageID)[1].lines

#		print self.newsgroup.article(self.messageID)
		headers = self.newsgroup.head(self.messageID)[1].lines
		self.body = (b'\r\n'.join(self.newsgroup.body(self.messageID)[1].lines)).decode('latin_1')
		
		# see email.message for full details of implementation
		###################
		# Sample Message: #
		###################
		# Path: dcs-news1.cs.illinois.edu!.POSTED!not-for-mail
		# From: Jeff <jkremer3@illinois.edu>
		# Newsgroups: class.fa10.cs225
		# Subject: Re: 2 Q's about Graph implementations
		# Date: Wed, 08 Dec 2010 23:50:30 -0600
		# Organization: Department of Computer Science, University of Illinois
		# Lines: 49
		# Sender: jkremer3@host-8-221.ilcu3rd.clients.pavlovmedia.com
		# Message-ID: <idpqn7$nuk$1@dcs-news1.cs.illinois.edu>
		# References: <idpo07$kkp$1@dcs-news1.cs.illinois.edu>
		# NNTP-Posting-Host: host-8-221.ilcu3rd.clients.pavlovmedia.com
		# Mime-Version: 1.0
		# Content-Type: text/plain; charset=ISO-8859-1; format=flowed
		# Content-Transfer-Encoding: 7bit
		# X-Trace: dcs-news1.cs.illinois.edu 1291873831 24532 216.171.8.221 (9 Dec 2010 05:50:31 GMT)
		# X-Complaints-To: abuse@cs.illinois.edu
		# NNTP-Posting-Date: Thu, 9 Dec 2010 05:50:31 +0000 (UTC)
		# User-Agent: Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.15) Gecko/20101027 Thunderbird/3.0.10
		# In-Reply-To: <idpo07$kkp$1@dcs-news1.cs.illinois.edu>
		# Xref: dcs-news1.cs.illinois.edu class.fa10.cs225:4002
		#
		# <payload (i.e. message body and/or attachments)>
		

		self.headers = email.message_from_string((b'\r\n'.join(headers)))

	def __del__(self):
		pass

	#####

