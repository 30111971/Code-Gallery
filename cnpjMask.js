export const cnpjMask = value => {
    return value.length >= 18 ? value.replace(value, value.substring(0, value.length-1)) : value
      .replace(/\D/g, '')
      .replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/g,"\$1.\$2.\$3\/\$4\-\$5")
}
