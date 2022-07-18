import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      email: ''
    },
    companyDetails: {
      id: 0,
      companyName: '',
      relationship: '',
      slug: '',
      city: '',
      country: '',
      address: '',
      businessType: '',
      businessLincese: '',
      tin: '',
      phone_number: 0,
      verified : false,

    }
  },

  // companyName = models.CharField(_("Manufacture Name"),max_length=160)
  // slug = models.SlugField(_("slug"),editable=False,unique=True,null=False)
  // accounttype = models.CharField(max_length=50,choices=ACCOUNTTYPE)
  // owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  // relationship = models.CharField(max_length=50,choices=relationshipToBusiness,default="Junior Employee",verbose_name=_("Relationship to Business"))
  // city = models.CharField(verbose_name=_("City"), max_length=50)
  // country = models.CharField(verbose_name=_("Country"), max_length=50)
  // phone_number = PhoneNumberField(verbose_name=_("Business Phone Number"))
  // address = models.TextField(verbose_name=_("Business Address"))
  // businessType = models.CharField(max_length=60, verbose_name=_("Business Type"),choices=businessStatus)
  // businessLincese = models.FileField(verbose_name=_("Bussiness Lincence"),help_text=_("Upload Business Lincence"),upload_to="upload/businesslicense/",null=True,blank=True)
  // tin = models.FileField(verbose_name=_("Tax Indentification"),help_text=_("Upload Tax Indentification"),upload_to="upload/tin/",null=True,blank=True)
  // verified = models.BooleanField(default=False)

  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('email')
        state.user.id = localStorage.getItem('userid')
        state.companyDetails.companyName = localStorage.getItem('companyname')
        state.companyDetails.id = localStorage.getItem('companyid')
        state.companyDetails.relationship = localStorage.getItem('relationship')
        state.companyDetails.slug = localStorage.getItem('slug')
        state.companyDetails.city = localStorage.getItem('city')
        state.companyDetails.country = localStorage.getItem('country')
        state.companyDetails.address = localStorage.getItem('address')
        state.companyDetails.businessType = localStorage.getItem('businessType')
        state.companyDetails.businessLincese = localStorage.getItem('businessLincese')
        state.companyDetails.tin = localStorage.getItem('tin')
        state.companyDetails.phone_number = localStorage.getItem('phone_number')
        state.companyDetails.verified = localStorage.getItem('verified')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
        state.companyDetails.id = 0
        state.companyDetails.companyName = ''
        state.companyDetails.relationship = ''
        state.companyDetails.slug = ''
        state.companyDetails.city = ''
        state.companyDetails.country = ''
        state.companyDetails.address = ''
        state.companyDetails.businessType = ''
        state.companyDetails.businessLincese = ''
        state.companyDetails.tin = ''
        state.companyDetails.verified = false
        state.companyDetails.phone_number = 0
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    
    setcompanyDetails(state, companyDetails) {
      state.companyDetails = companyDetails
      localStorage.setItem('companyid', companyDetails.id)
      localStorage.setItem('companyname', companyDetails.name)
      localStorage.setItem('slug', companyDetails.slug)
      localStorage.setItem('city', companyDetails.city)
      localStorage.setItem('country', companyDetails.country)
      localStorage.setItem('address', companyDetails.address)
      localStorage.setItem('businessType', companyDetails.businessType)
      localStorage.setItem('businessLincese', companyDetails.businessLincese)
      localStorage.setItem('tin', companyDetails.tin)
      localStorage.setItem('phone_number', companyDetails.phone_number)
      localStorage.setItem('verified', companyDetails.verified)
    }
  },
  actions: {
  },
  modules: {
  }
})