ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1( )

      IMPLICIT NONE

      INCLUDE 'model_functions.inc'
      INCLUDE '../vector.inc'


      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_3 = -(MDL_EE*MDL_COMPLEXI)
      GC_36 = MDL_EE*MDL_COMPLEXI*MDL_I25X33+MDL_EE*MDL_COMPLEXI
     $ *MDL_I26X33
      GC_246 = -(MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*(-1.000000D
     $ +00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))
      GC_250 = -((MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_SW)/((-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW)))
      GC_311 = -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_I97X33)/(2.000000D+00
     $ *(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))+(MDL_CW
     $ *MDL_EE*MDL_COMPLEXI*MDL_I101X33*MDL_SW)/((-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_I97X33
     $ *MDL_SW)/((-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      END
