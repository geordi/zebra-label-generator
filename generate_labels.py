import os


def generate_label(label):
    label_str = 'N\nA20,10,0,4,1,1,N,"room: {}"\nA20,50,0,4,1,1,N,"id: {}"\nA20,90,0,4,1,1,N,"sn: {}"\nP1'

    return label_str.format(label['room'], label['iid'], label['sn'])


def generate_labels_for_file(filename, room):
    labels = []
    with open(filename, 'rt') as f:
        for line in f:
            line = line.strip()
            print(line)
            if not line.startswith('#'):
                iid, _, name, sn, *_ = line.split(';')
                labels.append({'iid': iid, 'sn': sn, 'room': room})
    return labels


def generate_labels_for_files_in_dir(directory):
    filenames = os.listdir(directory)
    labels_out = []
    for filename in filenames:
        labels = generate_labels_for_file(os.path.join('data', filename), filename.split('.')[0].upper())
        labels = [generate_label(label) for label in labels]
        labels_out.extend(labels)

    return labels_out


def write_labels_to_file(labels, filename):
    with open(filename, 'wt') as f:
        for label in labels:
            f.write(label)
            f.write('\n')


def main():
    labels = generate_labels_for_files_in_dir('data')
    write_labels_to_file(labels, 'printable_labels.epl')


if __name__ == '__main__':
    main()

