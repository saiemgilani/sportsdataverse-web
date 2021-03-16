import React, { FC, ReactElement } from 'react'
import style from '../../styles/Footer.module.css'
import { Typography } from '@material-ui/core'

export const Footer: FC = ({}): ReactElement => {
  return (
    <div className={style.footer}>
      <Typography variant="body1" display="inline" className={style['footer-content']}>
        Copyright © 2021{' '}
        <a href="http://www.github.com/saiemgilani" target="_blank" rel="noreferrer">
          SportsDataverse.org
        </a>
      </Typography>
    </div>
  )
}
