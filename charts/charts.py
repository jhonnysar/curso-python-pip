import matplotlib.pyplot as plt

def generate_pie_chart():
    labels =['A','B','C']
    values =['200','34','120']
    
    values = [value for value in values]

    fig, ax = plt.subplots()
    ax.pie(values,labels=labels,autopct='%1.1f%%')
    plt.savefig('pie.png')
    plt.close()